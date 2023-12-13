import * as React from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import MenuIcon from '@mui/icons-material/Menu';
import PopupState, {bindTrigger, bindMenu } from 'material-ui-popup-state';
import { Link } from 'react-router-dom';
import './Menu.css';

export default function MenuPopupState() {
    return(
        <PopupState variant='popover' popupId='popup-menu'>
            {(popupState) => (
                <React.Fragment>
                    <MenuIcon variant='contained' {...bindTrigger(popupState)}>
                        Меню
                    </MenuIcon>
                    <Menu {...bindMenu(popupState)}>
                        <MenuItem onClick={popupState.close}>
                            <Link to='/createtask' className='link'>
                                Создать задачу
                            </Link>
                        </MenuItem>
                        <MenuItem onClick={popupState.close}>
                            <Link to='/mytask' className='link'>
                                Мои задачи
                            </Link>
                        </MenuItem>
                        <MenuItem onClick={popupState.close}>
                            <Link to='/dashboard' className='link'>
                                Дашборд
                            </Link>
                        </MenuItem>
                    </Menu>
                </React.Fragment>
            )}
        </PopupState>
    );
}