import React from 'react';
import API from './api'

export default class GroupList extends React.Component {
  state = {
    groups: []
  }

  async componentDidMount() {
    let user_id = '5fad563213d4b593894f7eea'
    let token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDUyMDg0MDAsImlkIjoiNWZhZDU2MzIxM2Q0YjU5Mzg5NGY3ZWVhIn0.ncoI-_nsiuJuXeFdv2oumJUnS-V1mElOsWjZde4zMD8'
    const response = await API.get(`user/${user_id}/groups`, {
      headers: {
        'Authorization': token
      }
    })
    let groups = response.data.data
    this.setState({ groups })
  }

  render() {
    return (
      <ul>
        { this.state.groups.map( (group, idx) => <li key={idx}> {group._id} </li>)}
      </ul>
    )
  }
}
