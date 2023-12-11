import React, { FunctionComponent, useState} from 'react';
import { FormControl, InputAdornment, TextField } from '@material-ui/core';
import { SearchSharp, ClearSharp } from '@mui/icons-material';
import { useStyles } from './useStyles';



const SearchInput: FunctionComponent = () => {
    const { search } = useStyles();

    const [showClearIcon, setShowClearIcon] = useState('none')
    const [value, setValue] = useState('')

    const handleClear = (e: any) => {
        setValue('');
        setShowClearIcon('none');
    }

    const handleChange = (e: any) => {
        setValue(e.target.value);
        setShowClearIcon(e.target.value === '' ? 'none' : 'flex');
    }

    return(
        <FormControl className={search}>
            <TextField
                size='small'
                variant='outlined'
                onChange={handleChange}
                value={value}
                InputProps={{
                    startAdornment: (
                        <InputAdornment position='start'>
                            <SearchSharp />
                        </InputAdornment>
                    ),
                    endAdornment: (
                        <InputAdornment
                            position='end'
                            style={{ display: showClearIcon }}
                            onClick={handleClear}
                        >
                            <ClearSharp/>
                        </InputAdornment>
                    )
                }}
            />
        </FormControl>
    );
}

export default SearchInput;