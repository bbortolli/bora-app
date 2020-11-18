import React, {useState} from 'react'
import API from './api'
import './App.css'

function Register (props) {

  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [re_password, setRePassword] = useState('')
  const [cpf, setCpf] = useState('')
  const [msg, setMsg] = useState(null)

  const form = {
    email: setEmail,
    password: setPassword,
    re_password: setRePassword,
    cpf: setCpf
  }

  const doRegister = (event) => {
    event.preventDefault()
    setMsg(null)
    API.post('user', {
      email, password, re_password, cpf
    }).then(res => {
      if (res.data.success) {
        setMsg('Registered !')
      } else {
        setMsg(res.data.err)
      }
    }).catch(err => {
      setMsg(err.response.statusText)
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
    <div className="form-box">
      <div className="form-input">
        <label htmlFor="email"><b>Email</b></label>
        <input type="text" placeholder="Email" name="email" value={email} onChange={handleChange} required/>
      </div>
      <div className="form-input">
        <label htmlFor="password"><b>Password</b></label>
        <input type="password" placeholder="Password" name="password" value={password} onChange={handleChange} required/>
      </div>
      <div className="form-input">
        <label htmlFor="re_password"><b>Re Password</b></label>
        <input type="password" placeholder="Re Password" name="re_password" value={re_password} onChange={handleChange} required/>
      </div>
      <div className="form-input">
        <label htmlFor="cpf"><b>CPF</b></label>
        <input type="text" placeholder="CPF" name="cpf" value={cpf} onChange={handleChange} required/>
      </div>
      <div className="form-input">
        <button type="submit" onClick={doRegister} disabled={!enableButton()}>Register</button>
      </div>
      {msg && (
        <p>{msg}</p>
      )}
    </div>
  )
}

export default Register;
