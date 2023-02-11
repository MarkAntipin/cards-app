import React from "react";
import { Routes, Route } from "react-router-dom";
import { DeckPage } from "./pages/Deck"
import { DeckCardsPage } from "./pages/DeckCards"
import { Desktop } from "./pages/Desktop"
import {isMobile} from 'react-device-detect';

class App extends React.Component {
  render() {
    if(isMobile) {
      return (
        <Routes>
          <Route path="/decks/:id" element={<DeckPage />} />
          <Route path="/decks/:id/cards" element={<DeckCardsPage />} />
          <Route path="*" element={<DeckPage />} />
        </Routes>
      )
    }
    else {
      return (
        <Desktop />
      )
    }
  }
}

export default App
