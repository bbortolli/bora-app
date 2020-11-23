import React from 'react'
import { Navbar, Nav } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { useAuth } from '../auth'

function Navigation () {

  const { authTokens, setAuthTokens } = useAuth();

  const doLogout = () => {
    localStorage.removeItem('tokens')
    setAuthTokens(null)
  }

  if (authTokens) {
    return (
      <Navbar expand="lg" sticky="top" bg="dark" variant="dark" className="justify-content-between px-4 py-3">
        <Nav>
          <Nav.Link as={Link} to="/home" style={{fontSize: '1.25em'}} className="ml-4 mr-4">Home</Nav.Link>
          <Nav.Link as={Link} to="/groups" style={{fontSize: '1.25em'}} className="mr-4">Groups</Nav.Link>
          <Nav.Link as={Link} to="/events" style={{fontSize: '1.25em'}} className="mr-4">Events</Nav.Link>
          <Nav.Link as={Link} to="/settings" style={{fontSize: '1.25em'}} className="mr-4">Settings</Nav.Link>
        </Nav>
        <Nav>
          <Nav.Link as={Link} to="/" style={{fontSize: '1.25em'}} className="mr-4" onClick={doLogout}>Logout</Nav.Link>
        </Nav>
      </Navbar>
    )
  } else {
    return (
      <Navbar expand="lg" sticky="top" bg="dark" variant="dark" className="justify-content-between px-4 py-3">
        <Nav>
          <Nav.Link as={Link} to="/login" style={{fontSize: '1.25em'}}>Login</Nav.Link>
          <Nav.Link as={Link} to="/signup" style={{fontSize: '1.25em'}}>Sign Up</Nav.Link>
        </Nav>
      </Navbar>
    )
  }
}

export default Navigation;
