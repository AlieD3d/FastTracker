import Toolbar from '@mui/material/Toolbar';
import Typography  from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AppBar  from '@mui/material/AppBar';
import MenuPopupState from '../Menu/Menu';
import SearchInput from '../SearchInput/SearchInput';

export default function Header() {
    return (
        <AppBar position='static'>
            <Toolbar>
                <IconButton
                    size='large'
                    edge='start'
                    color='inherit'
                    aria-label='menu'
                    sx={{ mx: 0 }}
                >
                    <MenuPopupState />
                </IconButton>
                <Typography
                    variant='h5'
                    component='div'
                    sx={{ flexGrow: 1, mr: 2 }}
                >
                    FastTracker
                </Typography>
                <SearchInput />
                <Button color='inherit'>Войти</Button>
            </Toolbar>
        </AppBar>
    );
}