import {createStyles, makeStyles} from "@material-ui/core";

export const useStyles = makeStyles(() => {
    return createStyles({
        search: {
            float: "right",
            overflow: "auto",
            padding: "0.8rem",
        }
    })
})