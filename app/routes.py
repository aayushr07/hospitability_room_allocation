from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
import pandas as pd
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group_file = request.files['group_file']
        hostel_file = request.files['hostel_file']

        if group_file and hostel_file:
            group_path = os.path.join('uploads', 'group_info.csv')
            hostel_path = os.path.join('uploads', 'hostel_info.csv')
            
            group_file.save(group_path)
            hostel_file.save(hostel_path)
            
            # Process files
            allocations = allocate_rooms(group_path, hostel_path)
            allocation_path = os.path.join('uploads', 'allocations.csv')
            allocations.to_csv(allocation_path, index=False)
            
            return render_template('index.html', allocations=allocations.to_dict(orient='records'))
        
        flash('Please upload both CSV files.')
        return redirect(url_for('main.index'))
    
    return render_template('index.html')

@main.route('/download_allocations', methods=['GET'])
def download_allocations():
    allocation_path = os.path.join('uploads','allocations.csv')
    return send_file(allocation_path,as_attachment=True)

def allocate_rooms(group_path, hostel_path):
    group_df = pd.read_csv(group_path)
    hostel_df = pd.read_csv(hostel_path)
    
    allocations = []
    
    for index, group in group_df.iterrows():
        group_id = group['Group ID']
        members = group['Members']
        gender = group['Gender']
        
        # Filter hostels by gender
        available_hostels = hostel_df[hostel_df['Gender'] == gender]
        
        # Find a suitable room
        for idx, room in available_hostels.iterrows():
            if room['Capacity'] >= members:
                allocations.append({
                    'Group ID': group_id,
                    'Hostel Name': room['Hostel Name'],
                    'Room Number': room['Room Number'],
                    'Members Allocated': members
                })
                hostel_df.at[idx, 'Capacity'] -= members
                break

    allocation_df = pd.DataFrame(allocations)
    return allocation_df