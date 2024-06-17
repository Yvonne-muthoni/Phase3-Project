// import {useState,useEffect}from 'react'
// import { NavLink } from 'react-router-dom'
// import { BASE_URL } from '../utils';

// function Card({drink}) {
//   const[categories,setCategories]=useState([]);
//   useEffect(()=>{
//     fetch(`${BASE_URL}/categories`,{
//       METHOD:'GET',
//       headers:{
//         'Content-Type':'application/json',

//       },
//     })
//     .then((res) => res.json())
// 			.then((data) => {
// 				setCategories(data);
// 			})
// 			.catch((err) => console.log(err));
// 	}, []);
//   return (
//     <div class ="card my-4 row-4 py-4"key={drink.id} style={{width:"18rem"}} >
//       <div className>
//         <img src = {drink.img} className =" col-10 text-center" alt="drinks.title" />
//         <div class="card-body text-center">
//         </div>
//         <NavLink to="/buy" className="btn btn-outline-primary">
//               Buy Now
//             </NavLink>
//             </div>
//     </div>
//     );

//   }

 


// export default Card