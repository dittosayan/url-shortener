import React,{ useState } from 'react';
import './InputForm.css';
import axios from 'axios';


const InputForm = () => {
    const [url, seturl] = useState("");
    const [short,setShort]=useState("");

    const shortenedLink = () => {
        if(short==="")
            return <></>;

        return(
            <div className="shortened-url">
                <p>Link : </p>
                <a href={short} id="shortened-link">
                    {short}
                </a>
                <button type="button" onClick={()=>{}}>Copy</button>
            </div>
        );
    }

    return (
        <>
        <div className="url">
            <span className="url-https">https://</span>
            <input type="text" className="url-text" onChange={(e)=>{seturl(e.target.value)}}>
            </input>
            
            <input type="submit" className="url-submit-button" onClick={()=>{
                axios.post("https://peepee-url.herokuapp.com/",{"url":url})
                .then( (response) => {
                    var shortenedUrl=response.data;
                    setShort(shortenedUrl);
                    console.log(response.data);
                })
            }}>
            </input>
            {shortenedLink()}
        </div>
        </>
    );
}

export default InputForm;
