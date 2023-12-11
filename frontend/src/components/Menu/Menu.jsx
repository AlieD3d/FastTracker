import * as React from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import MenuIcon from '@mui/icons-material/Menu';
import PopupState, {bindTrigger, bindMenu } from 'material-ui-popup-state';

export default function MenuPopupState() {
    return(
        <PopupState variant='popover' popupId='popup-menu'>
            {(popupState) => (
                <React.Fragment>
                    <MenuIcon variant='contained' {...bindTrigger(popupState)}>
                        Меню
                    </MenuIcon>
                    <Menu {...bindMenu(popupState)}>
                        <MenuItem onClick={popupState.close}>Создать задачу</MenuItem>
                        <MenuItem onClick={popupState.close}>Мои задачи</MenuItem>
                        <MenuItem onClick={popupState.close}>Дашборд</MenuItem>
                    </Menu>
                </React.Fragment>
            )}
        </PopupState>
    );
}