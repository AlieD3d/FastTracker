import Userfront from "@userfront/react";

Userfront.init("demo1234");

const LoginForm = Userfront.build({
    toolId: "alnkkd"
})

export default function Login(){
    return(
        <div className="outer">
            <LoginForm/>
        </div>
    );
}