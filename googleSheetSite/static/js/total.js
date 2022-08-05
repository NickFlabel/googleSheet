
let getTotalData = async() => {
// This function gets the total data from the api
    let location = window.location.href
    let response = await fetch(location + '/api/total')
    let data = await response.json()
    return data
}

class TotalData extends React.Component {
// This component builds the table and accepts the fetched JSON sheet data from API
    constructor(props) {
        super(props)
    }
    render() {
        return (
        <div className="card">
            <div className="card-body">
                <p className="card-text">Всего: {this.props.total_sum} $</p>
            </div>
        </div>
        )
    }
}

let mainLoop2 = () => {
    getTotalData().then(function(result) {
        ReactDOM.render(<TotalData total_sum={result.total_sum} />, document.getElementById('total'))
    }).then(setTimeout(mainLoop, 10000))
}

mainLoop2()
