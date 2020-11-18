import React, { useState } from 'react'
import { Redirect } from 'react-router-dom'

// import GroupList from './GroupList'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Navigation from './Navigation'
import Login from './Login'
import Register from './Register'
import Profile from './Profile'
import Groups from './Groups'
import Settings from './Settings'
import PrivateRoute from './PrivateRoute'
import { AuthContext } from './auth'

import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'

function App() {

  const existingTokens = JSON.parse(localStorage.getItem('tokens'))
  const [authTokens, setAuthTokens] = useState(existingTokens)

  const setTokens = (data) => {
    localStorage.setItem('tokens', JSON.stringify(data))
    setAuthTokens(data);
  }

  function Index () {
    return <Redirect to="/login" />
  }

  return (
    <AuthContext.Provider value={{ authTokens, setAuthTokens: setTokens }}>
      <Router>
        <Navigation/>
        <Switch>
          <Route exact path="/" component={Index} />
          <Route path="/login" component={Login} />
          <Route path="/signup" component={Register} />
          <PrivateRoute path="/home" component={Profile} />
          <PrivateRoute path="/groups" component={Groups} />
          <PrivateRoute path="/settings" component={Settings} />
        </Switch>
      </Router>
    </AuthContext.Provider>
  )
}

export default App;
