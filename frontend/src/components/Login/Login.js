import React from "react";
import {
    MDBBtn,
    MDBContainer,
    MDBCard,
    MDBCardBody,
    MDBCardImage,
    MDBRow,
    MDBCol,
    MDBIcon,
    MDBInput
}
from 'mdb-react-ui-kit';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import "@fortawesome/fontawesome-free/css/all.min.css";


export default function Login(){
    return(
        <MDBContainer className="my-5">

            <MDBCard>
                <MDBRow className="g-0">

                    <MDBCol md='6'>
                    <MDBCardImage src='https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp' alt="login form" className='rounded-start w-100'/>
                    </MDBCol>

                    <MDBCol md='6'>
                        <MDBCardBody className="d-flex flex-column">

                            <div className="d-flex flex-row mt-2">
                                <MDBIcon fas icon="cubes fa-3x me-3" style={{ color: '#ff6219' }}/>
                                <span className="h1 fw-bold mb-0">FastTracker</span>
                            </div>

                            <h5 className="fw-normal my-4 pb-3" style={{ letterSpacing: '1px' }}>
                                Войдите в свой аккаунт
                            </h5>

                            <MDBInput wrapperClass="mb-4" label='Адрес электронной почты' id="formControlling" type="email" size="lg" />
                            <MDBInput wrapperClass="mb-4" label='Пароль' id="formControlling" type="email" size="lg" />

                            <MDBBtn className="mb-4 px-5" color="dark" size="lg">Войти</MDBBtn>
                            <a className="small text-muted" href="#">Забыли пароль?</a>
                            <p className="mb-5 pb-lg-2" style={{color: '#393f81'}}>Ещё нет аккаунта? <a href="/signup" style={{color: '#393f81'}}>Регистрация</a></p>

                            <div className='d-flex flex-row justify-content-start'>
                                <a href="#" className="small text-muted">Политика конфиденциальности</a>
                            </div>

                        </MDBCardBody>
                    </MDBCol>
                </MDBRow>
            </MDBCard>
        </MDBContainer>
    );
}