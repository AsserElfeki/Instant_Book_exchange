<template>
  <div class="navbar">
    <img class="logo" alt="Bookz logo" src="@/assets/logo.png">
    <h class="signboard"> Bookz</h>
    <h class="undertext"> Book xchange website</h>
    <div class="wrap">
      <div class="search">
        <input type="text" class="searchTerm" placeholder="Type">
        <button type="submit" class="searchButton">
        </button>
        <img class="searchlogo" alt="search glass" src="@/assets/search.png">
      </div>
    </div>
    <button @click="login" class="button"> Sign in
    </button>
    <button @click="register" class="register"> Register
    </button>
  </div>
  <div>
    <img class="bgrectangle" alt="Background rectangle" src="@/assets/bgrectangle.png">
    <h class="randombk"> #RANDOM BOOK</h>
    <h1 class="mba">The Visual MBA</h1>
    <h2 class="upperau">by Jason Barron</h2>
    <img class="bgellipse" alt="Background ellipse" src="@/assets/bgellipse.png">
    <img class="bgdwnellipse" alt="Background down ellipse" src="@/assets/bgdwnellipse.png">
    <img class="bgmba" alt="Background mba text" src="@/assets/bgmba.png">
    <h1 class="mba2">The Visual MBA</h1>
    <h2 class="jason"> Jason Barron</h2>
    <button class="readmore">
      <router-link to="/"> Read more</router-link>
    </button>
  </div>
  <div>
    <h class="reviewboard"> Books</h>
    <img class="bgstartup" alt="Background startup" src="@/assets/bgstartup.png">
    <h3 class="bkstartup">The Lean Startup</h3>
    <p class="austartup">Eric Ries</p>
    <!---->
    <img class="bgrework" alt="Background rework" src="@/assets/bgrework.png">
    <h3 class="bkrework">Rework</h3>
    <p class="aurework">Jason Fried</p>
    <!---->
    <img class="bghabits" alt="Background habits" src="@/assets/bgmba.png">
    <h3 class="bkhabits">Atomic Habits</h3>
    <p class="auhabits">James Clear</p>
    <!---->
    <img class="bgartist" alt="Background artist" src="@/assets/bgartist.png">
    <h3 class="bkartist">Steal Like an Artist</h3>
    <p class="auartist">Austin Kleon</p>
    <!---->
    <img class="bgwork" alt="Background work" src="@/assets/bgwork.png">
    <h3 class="bkwork">Show Your Work!</h3>
    <p class="auwork">Austin Kleon</p>
    <!--stars-->
  </div>
  <router-view/>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      // tasks
      tasks: ['']
    }
  },
  methods: {
    async register() {
      try {
        let data = {
          "username": "qwerty",
          "password": "qwerty123#",
          "password2": "qwerty123#",
          "email": "admin4@gmail.com",
          "first_name": "Viktor",
          "last_name": "Moustafa",
        }
        const response = await axios.post('http://localhost:8000/authentication/register/', data);
        console.log(response.data);
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async login() {
      try {
        let data = {
          "username": "root",
          "password": "root",
        }
        const response = await axios.post('http://localhost:8000/authentication/login/', data);
        console.log(response.data["access"]);
        const headers = {"Authorization": "Bearer "+response.data["access"]} // Token should be in data, access token is required
        await this.whatever(headers); // Send access token to all further requests
        // return response.data["access"];
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async whatever(headers) {
      console.log("whatever");
      const response = await axios.get('http://localhost:8000/data/shelf/wanted', {headers});
      console.log(response.data);
    },
  },
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.logo {
  position: absolute;
  height: 45px;
  width: 45px;
  left: 159px;
  top: 33px;
  border-radius: 0px;
}

.navbar {
  position: absolute;
  width: 1920px;
  height: 107px;
  left: 0px;
  top: 0px;
}

.signboard {
  position: absolute;
  width: 117px;
  height: 35px;
  left: 232px;
  top: 23px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 700;
  font-size: 33px;
  line-height: 44px;
  color: #04040D;
}

.undertext {
  position: absolute;
  width: 135px;
  height: 19px;
  left: 235px;
  top: 64px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 400;
  font-size: 13px;
  line-height: 17px;
  color: #5C5969;
}

.search {
  width: 100%;
  position: absolute;
  display: flex;
}

.searchTerm {
  width: 879px;
  height: 34px;
  left: 562px;
  top: 30px;
  border: 0.5px solid #D0CAE9;
  border-right: none;
  padding: 5px;
  border-radius: 10px;
  outline: none;
}

.searchTerm:focus {
  color: #380136;
}

.searchButton {
  width: 40px;
  height: 59px;
  border: 0;
  background: #FFFFFF;
  text-align: center;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  font-size: 20px;
}

.wrap {
  width: 30%;
  position: absolute;
  top: 31%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.searchlogo {
  height: 29px;
  width: 30.07px;
  left: 1391px;
  top: 39px;
  border-radius: 0px;
}

.button {
  position: absolute;
  width: 139px;
  height: 47px;
  left: 1465px;
  top: 30px;
  background: #F2F0FE;
  border-radius: 10px;
  border: none;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 9px;
  align-items: center;
}

.button a {
  text-decoration: none;
  color: #695AC9;
}

.readmore {
  position: absolute;
  border: 0;
  width: 201px;
  height: 47px;
  left: 290px;
  top: 586px;
  background: #695AC9;
  border-radius: 10px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 24px;
  display: flex;
  align-items: center;
  display: block;
  text-align: center;
}

.readmore a {
  text-decoration: none;
  color: #F2F0FE;
}

.register {
  position: absolute;
  background-color: #695AC9;
  border-radius: 10px;
  width: 139px;
  height: 45px;
  left: 1628px;
  top: 33px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 24px;
  display: inline-block;
  align-items: center;
  text-align: center;
  border: 0;
  font-family: 'Segoe UI';
}

.register a {
  text-decoration: none;
  color: #F2F0FE;
}

.bgrectangle {
  position: absolute;
  width: 1614px;
  height: 609px;
  left: 153px;
  top: 144px;
  border-radius: 30px;
}

.bgellipse {
  position: absolute;
  width: 575px;
  height: 268px;
  left: 1192px;
  top: 146px;
  border-top-right-radius: 30px;
}

.bgdwnellipse {
  position: absolute;
  width: 402px;
  height: 120;
  left: 1044px;
  top: 633px;
}

.randombk {
  position: absolute;
  width: 379px;
  height: 76px;
  left: 290px;
  top: 242px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 400;
  font-size: 22px;
  line-height: 29px;
  color: #493F8E;
}

.mba {
  position: absolute;
  width: 379px;
  height: 64px;
  left: 290px;
  top: 318px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 700;
  font-size: 45px;
  line-height: 60px;
  color: #04040D;
}

.mba2 {
  position: absolute;
  width: 225.98px;
  height: 150.28px;
  left: 1279.68px;
  top: 288.75px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 900;
  font-size: 50.0943px;
  line-height: 68px;
  color: #04040D;
}

.bgmba {
  position: absolute;
  width: 293.89px;
  height: 413px;
  left: 1245.17px;
  top: 242px;
  background: #F9AB00;
  box-shadow: 3.33962px 8.90566px 44.5283px 4.45283px rgba(99, 87, 176, 0.35);
  border-radius: 18.9245px;
}

.jason {
  position: absolute;
  width: 225.98px;
  height: 44px;
  left: 1285.25px;
  top: 558.15px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 33.3962px;
  line-height: 1px;
  color: #5A5A5A;
}

.upperau {
  position: absolute;
  width: 379px;
  height: 45px;
  left: 290px;
  top: 382px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 28px;
  line-height: 37px;
  color: #5C5969;
}

.reviewboard {
  position: absolute;
  width: 379px;
  height: 64px;
  left: 153px;
  top: 830px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 53px;
  color: #04040D;
}

.bgstartup {
  position: absolute;
  width: 217px;
  height: 304.95px;
  left: 198px;
  top: 943px;
  box-shadow: 0px 5px 30px 1px rgba(99, 87, 176, 0.25);
  border-radius: 13.9735px;
}

.bkstartup {
  position: absolute;
  width: 166.86px;
  height: 110.97px;
  left: 223.48px;
  top: 949.52px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 900;
  font-size: 36.9886px;
  line-height: 50px;
  color: #FFFFFF;
}

.austartup {
  position: absolute;
  width: 166.86px;
  height: 33px;
  left: 227.59px;
  top: 1156.44px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 24.6591px;
  line-height: 33px;
  color: #FFFFFF;
}

.bgrework {
  position: absolute;
  width: 217px;
  height: 304.95px;
  left: 524px;
  top: 941px;
  box-shadow: 0px 5px 30px 1px rgba(99, 87, 176, 0.25);
  border-radius: 13.9735px;
}

.bkrework {
  position: absolute;
  width: 166.86px;
  height: 110.97px;
  left: 549.48px;
  top: 949.52px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 900;
  font-size: 36.9886px;
  line-height: 50px;
  color: #FFFFFF;
}

.aurework {
  position: absolute;
  width: 166.86px;
  height: 33px;
  left: 553.59px;
  top: 1156.44px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 24.6591px;
  line-height: 33px;
  color: #FFFFFF;
}

.bghabits {
  position: absolute;
  width: 217px;
  height: 304.95px;
  left: 850px;
  top: 939px;
  box-shadow: 0px 5px 30px 1px rgba(99, 87, 176, 0.25);
  border-radius: 13.9735px;
}

.bkhabits {
  position: absolute;
  width: 166.86px;
  height: 110.97px;
  left: 875.48px;
  top: 949.52px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 900;
  font-size: 36.9886px;
  line-height: 50px;
  color: #04040D;
}

.auhabits {
  position: absolute;
  width: 166.86px;
  height: 33px;
  left: 879.59px;
  top: 1156.44px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 24.6591px;
  line-height: 33px;
  color: #5A5A5A;
}

.bgartist {
  position: absolute;
  width: 217px;
  height: 304.95px;
  left: 1176px;
  top: 937px;
  box-shadow: 0px 5px 30px 1px rgba(99, 87, 176, 0.25);
  border-radius: 13.9735px;
}

.bkartist {
  position: absolute;
  width: 166.86px;
  height: 110.97px;
  left: 1201.48px;
  top: 949.52px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 900;
  font-size: 36.9886px;
  line-height: 50px;
  color: #FFFFFF;
}

.auartist {
  position: absolute;
  width: 166.86px;
  height: 33px;
  left: 1205.59px;
  top: 1156.44px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 24.6591px;
  line-height: 33px;
  color: #FFFFFF;
}

.bgwork {
  position: absolute;
  width: 217px;
  height: 304.95px;
  left: 1502px;
  top: 935px;
  box-shadow: 0px 5px 30px 1px rgba(99, 87, 176, 0.25);
  border-radius: 13.9735px;
}

.bkwork {
  position: absolute;
  width: 166.86px;
  height: 110.97px;
  left: 1527.48px;
  top: 949.52px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 900;
  font-size: 36.9886px;
  line-height: 50px;
  color: #FFFFFF;
}

.auwork {
  position: absolute;
  width: 166.86px;
  height: 33px;
  left: 1531.59px;
  top: 1156.44px;
  font-family: 'Segoe UI';
  font-style: normal;
  font-weight: 600;
  font-size: 24.6591px;
  line-height: 33px;
  color: #FFFFFF;
}
</style>
