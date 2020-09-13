import React from 'react';
import axios from 'axios'
import { Doughnut } from 'react-chartjs-2';
import { RGBA } from './rgbaColor'

import './App.css';

const API_PROTOCOL = process.env.REACT_APP_API_PROTOCOL || 'http'
const API_HOST = process.env.REACT_APP_API_HOST || 'localhost'
const API_PORT = process.env.REACT_APP_API_PORT || 5000

class App extends React.Component {
  state = {
    qualifyingOffer: {},
    salaries: []
  }

  async componentDidMount() {
    return this.getDataFromApi()
  }

  async getDataFromApi() {
    const response = await axios.get(`${API_PROTOCOL}://${API_HOST}:${API_PORT}/v1/qualifying-offer`)
    this.setState((state) => {
      return {
        qualifyingOffer: response.data.qualifying_offer,
        salaries: response.data.salaries
      }
    })
  }

  getNumberOfSalariesBelowQualifyingOffer() {
    const qualifyingOffer = this.state.qualifyingOffer
    const salariesBelowQO = this.state.salaries.filter((e) => e < qualifyingOffer.value)
    return salariesBelowQO.length
  }

  render() {
    const salariesBelowQO = this.getNumberOfSalariesBelowQualifyingOffer()
    const salariesAboveQO = this.state.salaries.length - salariesBelowQO

    const blue = new RGBA(8, 83, 204, 0.75)
    const red = new RGBA(204, 8, 8, 0.75)

    return (
      <div className="app">
        <header className="header">
          {/* <img src="https://seekvectorlogo.net/wp-content/uploads/2018/08/philadelphia-phillies-vector-logo.png"></img> */}
        </header>
        
        <div className="qo-banner">
          <div className="offer-label">
            { this.state.qualifyingOffer.label }
          </div>
          <div className="subhead">
            2016 Qualifying Offer
          </div>
        </div>

        <div className="chart-wrap">
          <Doughnut 
            data={
              {
                labels: [
                  'Salaries Greater Than Qualifying Offer',
                  'Salaries Less Than Qualifying Offer'
                ],
                datasets: [
                  {
                    data: [salariesAboveQO, salariesBelowQO],
                    backgroundColor:[red.getString(), blue.getString()],
                  }
                ]
              }
            }
            options={{ maintainAspectRatio: false, legend: { display: false, position: 'right' } }}
          ></Doughnut>
        </div>
        
        <footer>
          <a href={`${API_PROTOCOL}://${API_HOST}:${API_PORT}/v1/ui`}>API Documentation</a>
        </footer>
      </div>
    );
  }
}

export default App;
