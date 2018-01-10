import React, { Component } from 'react';
import Header from '../components/Header';


class HeaderContainer extends Component {
  constructor(props) {
    super(props);
    this.API_URL = '/sso/session_user?format=json';
    this.state = {
      username: 'ohno',
      staff: false,
      committee: true,
    };
    this.fetchUser();
  }

  fetchUser() {
    const apiUrl = this.API_URL;
    fetch(apiUrl, { credentials: 'same-origin' })
    .then(response => response.json())
    .then((results) => {
      this.setState({
        username: results.username,
        staff: results.staff,
        committee: results.committee,
      });
    });
  }

  render() {
    return (
      <Header username={this.state.username} staff={this.state.staff} committee={this.state.committee} />
    );
  }
}

export default HeaderContainer;
