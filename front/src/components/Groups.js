import React, { useState, useEffect, useRef } from 'react'
import { Row, Col, Card, Button, Spinner } from 'react-bootstrap'
import API from '../api'
import { useAuth } from '../auth'

function Groups () {

  const { authTokens } = useAuth();
  const [groups, setGroups] = useState(null)
  const [isLoading, setLoading] = useState(true)
  const mounted = useRef(true);

  useEffect(() => {
    mounted.current = true
    if (groups) {
      return
    }
    API.get('groups', {
      headers: {
        'Authorization': authTokens
      }
    }).then(res => {
      setGroups(res.data.groups)
      setLoading(false)
    }).catch(err => {
      console.log('err')
    })
    return () => mounted.current = false
  }, [authTokens, groups])

  const itemGroup = (group, idx) => {
    return (
      <Col sm={3} key={idx}>
        <Card style={{ margin: '15px' }}>
          <Card.Img variant="top" src="https://soumaislagoa.com.br/wp-content/uploads/2019/11/48413389_2231106680471116_9000997253246091264_o.jpg" />
          <Card.Body>
            <Card.Title>{group.name}</Card.Title>
            <Card.Text style={{ marginBottom: '1px'}}>From: {group.from_location}</Card.Text>
            <Card.Text style={{ marginBottom: '1px'}}>To: {group.to_location}</Card.Text>
            <Button onClick={() => console.log(group._id)} style={{ marginTop: '5px'}} variant="primary">Open</Button>
          </Card.Body>
        </Card>
      </Col>
    )
  }
  if (groups && groups.length) {
    return (
      <Row sm={4} className="mx-4 my-4">
        { groups.map( (group, idx) => itemGroup(group, idx)) }
      </Row>
    )
  } else if (groups && !groups.length) {
    return (
      <h1 className="mx-4 my-4">0 Groups!</h1>
    )
  } else if (isLoading) {
    return <Spinner style={{width: '100px', height: '100px'}} animation="border" className="abs-center"/>
  }
}

export default Groups;
