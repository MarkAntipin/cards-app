const Logo = () => {

  return (
    <div
      className="center"
      style={{
        marginBottom: "5vh",
      }}
    >
      <img
        style={{
          width: "20vh",
          height: "20vh",
        }}
        src={require("../images/logo_sko.png")}
        alt={"logo"}
      />
    </div>
  )
}

export { Logo }
