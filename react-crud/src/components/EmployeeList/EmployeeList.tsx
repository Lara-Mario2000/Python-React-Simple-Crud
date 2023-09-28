import React from 'react';
import Employee, { EmployeeProps } from '../Employee/Employee';
import '../EmployeeList/EmployeeList.css'

interface EmployeeListProps {
  employees: EmployeeProps[];
}

const EmployeeList: React.FC<EmployeeListProps> = ({ employees }) => {
  return (
    <div className="employee-list">
      {Array.isArray(employees) && employees.length > 0 ? (
        employees.map((employee) => (
          <Employee key={employee.id} {...employee} />
        ))
      ) : (
        <p>No hay empleados disponibles.</p>
      )}
    </div>
  );
};

export default EmployeeList;
