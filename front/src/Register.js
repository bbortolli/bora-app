import React, { useState } from 'react'
import { Container, Form, Col, Row, Card, Button, Alert, Spinner } from 'react-bootstrap'

import API from './api'
import './App.css'

function Register (props) {

  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [re_password, setRePassword] = useState('')
  const [cpf, setCpf] = useState('')
  const [msg, setMsg] = useState(null)
  const [isLoading, setLoading] = useState(false)

  const form = {
    email: setEmail,
    password: setPassword,
    re_password: setRePassword,
    cpf: setCpf
  }

  const doRegister = (event) => {
    event.preventDefault()
    setMsg(null)
    setLoading(true)
    API.post('user', {
      email, password, re_password, cpf
    }).then(res => {
      setLoading(false)
      if (res.data.success) {
        setMsg('Registered !')
      } else {
        setMsg(res.data.err)
      }
    }).catch(err => {
      setLoading(false)
      setMsg(err.response ? err.response.statusText : 'Unknown error !')
    })
  }

  const handleChange = (event) => {
    const {name, value} = event.target
    form[name](value)
  }

  const enableButton = () => {
    let validEmail = email.length >= 10
    let validPw = password.length >= 8 && re_password.length >= 8 && password === re_password
    let validCpf = cpf.length === 11
    return validEmail && validPw && validCpf
  }

  return (
    <Container>
      <Row className="justify-content-md-center mt-4">
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title style={{textAlign: 'center'}}>Sign Up</Card.Title>
            <Form>
              <Form.Group as={Row}>
                <Col sm={12}>
                  <Form.Control type="email" placeholder="Email" name="email" onChange={handleChange} />
                </Col>
              </Form.Group>
              <Form.Group as={Row}>
                <Col sm={12}>
                  <Form.Control type="password" placeholder="Password" name="password" onChange={handleChange} />
                </Col>
              </Form.Group>
              <Form.Group as={Row}>
                <Col sm={12}>
                  <Form.Control type="password" placeholder="Repeat Password" name="re_password" onChange={handleChange} />
                </Col>
              </Form.Group>
              <Form.Group as={Row}>
                <Col sm={12}>
                  <Form.Control type="text" placeholder="CPF" name="cpf" onChange={handleChange} />
                </Col>
              </Form.Group>
            </Form>
            <Row>
              { msg &&
                <Col>
                  <Alert variant="dark"> { msg } </Alert>
                </Col>
              }
              { isLoading &&
                <Col className="d-flex justify-content-center mb-3">
                  <Spinner animation="border" variant="success" size="md"/>
                </Col>
              }
            </Row>
            <Row>
              <Col>
                <Button variant="dark" style={{width: '100%'}} onClick={doRegister} disabled={!enableButton()}>Register</Button>
              </Col>
            </Row>
          </Card.Body>
        </Card>
      </Row>
    </Container>
  )
}

export default Register;
