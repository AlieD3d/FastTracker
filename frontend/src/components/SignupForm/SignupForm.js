import React from "react";
import Userfront from "@userfront/react"
import './style.css'

Userfront.init("demo1234")

const SignupForm = Userfront.build({
    toolId: "nkmbbm"
})

function Signup() {
    return(
        <div className="outer">
            <SignupForm/>
        </div>
    );
}

export default Signup;