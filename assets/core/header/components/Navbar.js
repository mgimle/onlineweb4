import React from 'react';

const Navbar = () => (
  <ul className="Navbar">
    <li className="Navbar__item">
      <a className="Navbar__item-text" href="/events/">Arkiv</a>
    </li>
    <li className="Navbar__item">
      <a className="Navbar__item-text" href="/careeropportunity/">Karriere</a>
    </li>
    <li className="Navbar__item">
      <a className="Navbar__item-text" href="/resourcecenter/">Ressurser</a>
    </li>
    <li className="Navbar__item">
      <a className="Navbar__item-text" href="/hobbygroups/">Interessegrupper</a>
    </li>
    <li className="Navbar__item">
      <a className="Navbar__item-text" href="/wiki/">Wiki</a>
    </li>
    <li className="Navbar__item">
      <a className="Navbar__item-text" href="/webshop/">Webshop</a>
    </li>
  </ul>
);

export default Navbar;
