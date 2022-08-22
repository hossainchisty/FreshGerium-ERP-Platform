

class Greeting extends React.Component {
    render() {
        const currentTime = new Date().getHours();
        return (
            <>
                <span>
                    Good{" "}
                    {currentTime >= 12
                        ? currentTime >= 16
                            ? "Evening🌃"
                            : "Afternoon🌇"
                        : "Morning🌅"}
                </span>
            </>
        );
    }
}

ReactDOM.render(<Greeting />, document.getElementById("greeting"));