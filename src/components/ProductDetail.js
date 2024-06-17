import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router';
import { useDispatch, useSelector } from 'react-redux';
import { addItem, delItem } from '../redux/actions/index';

const ProductDetail = () => {
    const [product, setProduct] = useState(null);
    const [cartBtn, setCartBtn] = useState("Add to Cart");
    const { id } = useParams();
    const dispatch = useDispatch();

    // Assume your products data is already available in Redux store or passed as props
    const products = useSelector(state => state.products);
    const cartItems = useSelector(state => state.cartItems);

    useEffect(() => {
        // Check if products array is available
        if (!products) return;

        // Find the product with the given id from the products data
        const foundProduct = products.find(item => item.id === parseInt(id));
        if (foundProduct) {
            setProduct(foundProduct);
        }
    }, [id, products]);

    useEffect(() => {
        console.log("Cart Items:", cartItems);
    }, [cartItems]);

    const handleCart = () => {
        if (!product) return;
        if (cartBtn === "Add to Cart") {
            dispatch(addItem(product));
            setCartBtn("Remove from Cart");
        } else {
            dispatch(delItem(product));
            setCartBtn("Add to Cart");
        }
    };

    if (!product) {
        return <div>Loading...</div>;
    }

    return (
        <div className="container my-5 py-3">
            <div className="row">
                <div className="col-md-6 d-flex justify-content-center mx-auto product">
                    <img src={product.img} alt={product.title} height="400px" />
                </div>
                <div className="col-md-6 d-flex flex-column justify-content-center">
                    <h1 className="display-5 fw-bold">{product.title}</h1>
                    <hr />
                    <h2 className="my-4">${product.price}</h2>
                    <p className="lead">{product.desc}</p>
                    <button onClick={handleCart} className="btn btn-outline-primary my-5">{cartBtn}</button>
                </div>
            </div>
        </div>
    );
}

export default ProductDetail;
