import React, {useState} from 'react'
import { Redirect } from 'react-router-dom'
import { Container, Form, Col, Row, Card, Button } from 'react-bootstrap'
import API from './api'
import './App.css'
import { useAuth } from './auth'

function Login () {

  const [isLoggedIn, setLoggedIn] = useState(false)
  const { setAuthTokens } = useAuth();
  const [isLoading, setLoading] = useState(false)


  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [err, setErr] = useState(null)

  const form = {
    email: setEmail,
    password: setPassword
  }

  const doLogin = (event) => {
    event.preventDefault()
    setLoading(true)
    setErr(null)
    API.post('login', {
      email, password
    }).then(res => {
      setAuthTokens(res.data.jwt)
      setLoggedIn(true)
    }).catch(err => {
      setErr(err.response.statusText)
    })
    setLoading(false)
  }

  if (isLoggedIn) {
    return <Redirect to="/home" />
  }

  const goToRegister = () => {
    return <Redirect to="/signup" />
  }

  const handleChange = (event) => {
    const {name, value} = event.target
    form[name](value)
  }

  const enableButton = () => {
    return email.length >= 5 && password.length >= 8
  }

  return (
    <Container>
      <Row className="justify-content-md-center mt-4">
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>Login</Card.Title>
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
            </Form>
            <Row>
              <Col sm={6}>
                <Button variant="dark" onClick={doLogin} disabled={!enableButton()}>Login</Button>
              </Col>
            </Row>
          </Card.Body>
        </Card>
      </Row>
    </Container>
  )
}

export default Login
