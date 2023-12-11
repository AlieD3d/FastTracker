import * as React from 'react';
import CardArea from '../Card/CardArea';
import { Container } from '@mui/material';
import { useStyles } from './useStyles';
import './styler.css';


export default function Main(){
    const { container } = useStyles();

    return(
        <Container className={container}>
            <CardArea />
        </Container>
    );
}