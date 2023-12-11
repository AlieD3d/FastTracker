import * as React from 'react';
import Box from '@mui/material/Box';
import {DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';

const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 90 },
    {
        field: 'cataTasker',
        headerName: 'Категория задачи',
        width: 190,
        editable: true,
    },
    {
        field: 'author',
        headerName: 'Автор задачи',
        width: 120,
        editable: true,
    },
    {
        field: 'task',
        headerName: 'Задача',
        width: 255,
        editable: true,
    },
    {
        field: 'deadline',
        headerName: 'Срок выполнения',
        width: 150,
        type: 'number',
        editable: true,
    },
    {
        field: 'executor',
        headerName: 'Исполнитель',
        description: 'This column a value getter and is not sortable.',
        sortable: false,
        width: 160,
        valueGetter: (params: GridValueGetterParams) =>
            `${params.row.executor || ''}`
    }
];

const rows = [
    { id: 1, cataTasker: 'Важные задачи', author: 'Vasyan', task:'Сделать капчу', deadline: 10, executor: 'Mirai'},
    { id: 2, cataTasker: 'Средние задачи', author: 'Vasyan', task:'Сломана картинка', deadline: 12, executor: 'Mirai'},
    { id: 3, cataTasker: 'Незначительные задачи', author: 'Vasyan', task:'Overide', deadline: 9, executor: 'Mirai'},
]

export default function CardArea() {
    return(
        <Box sx={{ height: 400, width: '100%' }}>
            <DataGrid
                rows={rows}
                columns={columns}
                initialState={{
                    pagination: {
                        paginationModel: {
                            pageSize: 5,
                        },
                    },
                }}
                pageSizeOptions={[5]}
                checkboxSelection
                disableRowSelectionOnClick
            />
        </Box>
    );
}