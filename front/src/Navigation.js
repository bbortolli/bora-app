import React from 'react'
import { Navbar, Nav, InputGroup } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { useAuth } from './auth'

function Navigation () {

  const { authTokens, setAuthTokens } = useAuth();

  const doLogout = () => {
    localStorage.removeItem('tokens')
    setAuthTokens(null)
  }

  if (authTokens) {
    return (
      <Navbar bg="dark" variant="dark" className="justify-content-between">
        <InputGroup>
          <InputGroup.Prepend>
            <Navbar.Brand as={Link} to="/home">BORA !</Navbar.Brand>
            <Nav className="mr-auto">
              <Nav.Link as={Link} to="/home">Home</Nav.Link>
              <Nav.Link as={Link} to="/groups">Groups</Nav.Link>
              <Nav.Link as={Link} to="/settings">Settings</Nav.Link>
              <Nav.Link as={Link} to="/" onClick={doLogout}>Logout</Nav.Link>
            </Nav>
          </InputGroup.Prepend>
        </InputGroup>
      </Navbar>
    )
  } else {
    return (
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">BORA !</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link as={Link} to="/login">Login</Nav.Link>
          <Nav.Link as={Link} to="/signup">Sign Up</Nav.Link>
        </Nav>
      </Navbar>
    )
  }
}

export default Navigation;
