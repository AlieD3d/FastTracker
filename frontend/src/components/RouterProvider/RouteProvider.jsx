import React from "react";
import { Routes, Route } from 'react-router-dom';


export default function RouteProvider(){
    return(
        <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/reset" element={<PasswordReset/>} />
            <Route path="/dashboard" element={<Dashboard/>} />
            <Route path="/createtask" element={<CreateTask/>} />
            <Route path="/edittask" element={<EditTask/>} />
            <Route path="/mytask" element={<MyTask/>} />
        </Routes>
    );
}

function Login(){
    return <h2>Login</h2>
}

function PasswordReset() {
    return <h2>Password Reset</h2>
}

function Dashboard() {
    return <h2>Dashboard</h2>
}

function MyTask() {
    return <h2>My Task</h2>
}

function EditTask() {
    return <h2>Edit task: id</h2>
}

function CreateTask() {
    return <h2>Create Task</h2>
}

function Home(){
    return <h2>Home</h2>
}