
let getSheetData = async() => {
// This function gets the sheet data from the api
    let location = window.location.href
    let response = await fetch(location + '/api/sheet')
    let data = await response.json()
    return data
}

class SheetData extends React.Component {
    constructor(props) {
        super(props)
    }
    render() {
        let rows = []
        for (let i = 0; i < this.props.sheet.length; i++) {
            rows.push(<SheetRow row={this.props.sheet[i]} />)
        }
        return (
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Номер Заказа</th>
                        <th>Цена в долларах</th>
                        <th>Цена в рублях</th>
                        <th>Дата поставки</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        )
    }
}

class SheetRow extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return(
            <tr>
                <td> {this.props.row.number_in_table} </td>
                <td> {this.props.row.order_number} </td>
                <td> {this.props.row.price_in_dollars} $</td>
                <td> {this.props.row.price_in_rubles} </td>
                <td> {this.props.row.date_of_shipping} </td>
            </tr>
        )
    }
}


let mainLoop = () => {
    getSheetData().then(function(result) {
        ReactDOM.render(<SheetData sheet={result} />, document.getElementById('table-space'))
    }).then(setTimeout(mainLoop, 10000))
}

mainLoop()

