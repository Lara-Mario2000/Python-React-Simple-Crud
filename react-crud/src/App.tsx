import { useState, useEffect } from 'react';
import './App.css';
import EmployeeList from './components/EmployeeList/EmployeeList';

function App() {
  // Define un estado para los datos de los empleados
  const [employees, setEmployees] = useState([
    {
      id: 1,
      first_name: 'John',
      last_name: 'Doe',
      job_title: 'Developer',
      phone_number: '123-456-7890',
      image_url: 'https://cdn.discordapp.com/attachments/1115765550191214644/1156708433391779901/image.png?ex=6515f42d&is=6514a2ad&hm=d7f23d0044f19cf280c0ed2aad9a4d47537d4ecb9db313679bc7720590fbd2d3&',
    }
  ]);

  useEffect(() => {
    // Hacer una solicitud GET a tu API Flask
    fetch('http://127.0.0.1:5000/employee') // Asegúrate de que esta ruta coincida con la que tienes en tu servidor Flask
      .then((res) => res.json())
      .then((data) => {
        // Establecer los datos de empleados obtenidos de la API en el estado
        setEmployees(data.employees);
      })
      .catch((error) => {
        console.error('Error al obtener datos de la API:', error);
      });
  }, []);

  return (
    <>
      <div className="App">
        <h1>Lista de Usuarios</h1>
        <EmployeeList employees={employees} />
      </div>
    </>
  );
}

export default App;
