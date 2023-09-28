import React from 'react';
import '../Employee/Employee.css'

export interface EmployeeProps {
  id: number;
  first_name: string;
  last_name: string;
  job_title: string;
  phone_number: string;
  image_url: string;
}

const Employee: React.FC<EmployeeProps> = ({
  id,
  first_name,
  last_name,
  job_title,
  phone_number,
  image_url,
}) => {
  return (
    <div className="employee">
      <img src={image_url} alt={`${first_name} ${last_name}`} />
      <div className="employee-details">
        <p>{`${first_name} ${last_name}`}</p>
        <p>{job_title}</p>
        <p>{phone_number}</p>
      </div>
    </div>
  );
};

export default Employee;
