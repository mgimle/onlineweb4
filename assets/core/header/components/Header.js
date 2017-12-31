import React from 'react';
import Logo from './Logo';
import Navbar from './Navbar';
import Dropdown from './Dropdown';
import Sponsor from './Sponsor';

const Header = () => (
  <div className="Header">
    <div className="Header__container">
      <Logo />
      <Navbar />
      <Dropdown />
      <Sponsor />
    </div>
  </div>
);

export default Header;
