import {Link, useParams} from "react-router-dom"
import React, { useState, useEffect } from "react"
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import SwipeCard from "../components/SwipeCard";
import { creteRandomValue } from "../utils/creteRandomValue";
import {Logo} from "../components/Logo";

const DeckCardsPage = () => {
  const {id} = useParams();
  const [cards, setCards] = useState([]);

  useEffect(() => {
      fetch(process.env.REACT_APP_BACKEND_URL + `/api/v1/cards?deck_id=${id}`)
          .then(res => res.json())
          .then(data => setCards(data))
  }, [id]);

  let counter = cards.length - 1
  const swiped = () => {
    counter -= 1
  }


  return (
    <div className="background">
      <div
        style={{
          zIndex: 2
        }}
      >
        {cards.map((card) =>
          <SwipeCard
            className="swipe"
            key={card.id}
            onSwipe={() => swiped()}
          >
            <Card
              className="card"
              style={{
                transform: `rotate(${creteRandomValue(-1.5, 1.5, 0.2)}deg)`
              }}
            >
              <Card.Body>
                <Card.Text className="card-text">
                  {card.text}
                </Card.Text>
              </Card.Body>
              <Logo />
            </Card>
          </SwipeCard>
        )}
      </div>
      {counter >= 0 ? (
      <div>
        <div
          className="center"
          style={{
            marginTop: "15vh"
          }}
        >
          <p
            style={{
              color: "#FFFFFF",
              marginLeft: "5vh",
              marginRight: "5vh",
              fontSize: "3vh",
              fontFamily: "SourceSansPro",
            }}
          >
            Ой, конец! <br/>
            Мы надеемся, что игра помогла вам узнать друг друга чуточку лучше! <br/>
            Наш сайт совсем скоро пополниться новыми колодами для увлекательных бесед. <br/>
            Чтобы не пропустить обновления, подпишитесь на аккаунт в запрещенной социальной сети <a href="https://www.instagram.com/silno.krepko.ochen/">@silno.krepko.ochen</a>
          </p>
        </div>
        <div className="center">
          <Link to={`/decks/${id}`}>
            <Button
              className="card-title start-button"
              variant="light"
            >
              К колоде
            </Button>
          </Link>
        </div>
        </div>
        ) : (
          <div></div>
        )}
    </div>
  )
}

export { DeckCardsPage }
