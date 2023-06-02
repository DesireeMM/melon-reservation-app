function BookingTime(props) {
    return (
        <div className="booking-time">
            <button type="button" id={props.resDateTime} className="book-btn">{props.time}</button>
        </div>
    )
}

function BookingTimeContainer() {
    const [times, setTimes] = React.useState([]);

    React.useEffect(() => {
        fetch('/booking-times')
        .then((response) => response.json())
        .then((data) => {
            setTimes(data.avail_bookings);
        })
    }, [])
    
    console.log(times);

    const allBookingTimes = [];

    for (const currentTime of times) {
        allBookingTimes.push(
            <BookingTime 
            resDatetime={currentTime.resDatetime}
            resTime={currentTime.resTime}
            />
        )
    }
    console.log(allBookingTimes);

    return (
        <React.Fragment>
            <h2>Available Reservations</h2>
            <div className="grid">{allBookingTimes}</div>
        </React.Fragment>
    );
}

ReactDOM.render(<BookingTimeContainer />, document.getElementById('booking-container'));