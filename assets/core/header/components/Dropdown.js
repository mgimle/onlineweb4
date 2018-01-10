import React, { PropTypes, Component } from 'react';
import { Glyphicon } from 'react-bootstrap';


class Dropdown extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
    };
  }

  handleClick(e) {
    e.preventDefault();
    this.setState({
      isOpen: !this.state.isOpen,
    });
  }

  buildMenu() {
    if (!this.state.isOpen) {
      return null;
    }
    return (
      <div className="Dropdown__menu">
        <p>ho ho ho</p>
      </div>
    );
  }

  render() {
    const dropdownMenu = this.buildMenu();
    return (
      <div className="Dropdown">
        <a href="#login-menu" className="Dropdown__icon" onClick={e => this.handleClick(e)}>
          <Glyphicon glyph="user" />
        </a>
        {dropdownMenu}
      </div>
    );
  }
}

Dropdown.propTypes = {
  username: PropTypes.string.isRequired,
  staff: PropTypes.bool.isRequired,
  committee: PropTypes.bool.isRequired,
};

export default Dropdown;
