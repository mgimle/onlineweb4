import React, { PropTypes } from 'react';
import Logo from './Logo';
import Navbar from './Navbar';
import Dropdown from './Dropdown';
import Sponsor from './Sponsor';

const Header = ({ username, staff, committee }) => (
  <div className="Header">
    <div className="Header__container">
      <Logo />
      <Navbar />
      <Dropdown username={username} staff={staff} committee={committee} />
      <Sponsor />
    </div>
  </div>
);

Header.propTypes = {
  username: PropTypes.string.isRequired,
  staff: PropTypes.bool.isRequired,
  committee: PropTypes.bool.isRequired,
};

export default Header;
