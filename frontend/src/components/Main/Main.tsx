import * as React from 'react';
import CardArea from '../Card/CardArea';
import { Container } from '@mui/material';
import { useStyles } from './useStyles';
import './styler.css';
import RouteProvider from '../RouterProvider/RouteProvider';


export default function Main(){
    const { container } = useStyles();

    return(
        <RouteProvider />
    );
}