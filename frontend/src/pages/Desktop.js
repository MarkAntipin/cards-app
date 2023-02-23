import {Logo} from "../components/Logo";
import React from "react";

const Desktop = () => {

  return (
    <div>
      <p
        className="card-title center"
      >
        К вам пришли гости, а вы все еще за компьютером? <br/>
        Советуем вам воспользоваться мобильной версией через телефон, <br/>
        открыв наш сайт за столом в кругу друзей и близких!
      </p>
      <Logo />
    </div>

  )
}

export { Desktop }
