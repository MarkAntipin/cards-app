import { useParams, Link } from "react-router-dom"
import React, { useState, useEffect } from "react"
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import { creteRandomValue } from "../utils/creteRandomValue"
import {Logo} from "../components/Logo";

const DeckPage = () => {
  const { id = 1 } = useParams();
  const [deck, setDeck] = useState({});

  useEffect(() => {
      fetch(process.env.REACT_APP_BACKEND_URL + `/api/v1/decks/${id}`)
          .then(res => res.json())
          .then(data => setDeck(data))
  }, [id]);

  return (
    <div className="background">
      <Card
        className="mx-auto, card"
        style={{
          transform: `rotate(${creteRandomValue(-1.5, 1.5, 0.2)}deg)`
        }}
      >
        <Card.Body>
          <Card.Title className="card-title">
            {deck.title}
          </Card.Title>
          <Card.Text
            className="card-description"
            style={{
              fontSize: "3vh",
              marginTop: "3vh"
            }}
          >
            {deck.description}
          </Card.Text>
          <div className="center">
            <Link to={`/decks/${id}/cards`}>
              <Button
                className="bg-transparent, card-title start-button"
                variant="light"
              >
                Начать
              </Button>
            </Link>
          </div>
        </Card.Body>
        <Logo />
      </Card>
    </div>
  )
}

export { DeckPage }
