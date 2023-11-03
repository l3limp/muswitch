import "./App.css";
import { TextField, Button } from "@mui/material";
import { useState } from "react";
import axios from "axios";

function App() {
  const [name, setName] = useState("");
  const [oldPlaylistURL, setOldPlaylistURL] = useState("");
  const [convertFrom, setConvertFrom] = useState("");
  const [convertTo, setConvertTo] = useState("");
  const [returnURL, setReturnURL] = useState("");

  function handleClick() {
    var from = "";
    var to = "";
    if(convertFrom==='Y' || convertFrom ==='y') from = "YouTubeMusic";
    if(convertTo==='Y' || convertTo ==='y') to = "YouTubeMusic";
    if(convertFrom==='S' || convertFrom ==='s') from = "Spotify";
    if(convertTo==='S' || convertTo ==='s') to = "Spotify";

    // convert URL to ID
    let oldPlaylistID = "";
    if(from === "YouTubeMusic") oldPlaylistID = oldPlaylistURL.substring(34, 68);
    if(from === "Spotify") oldPlaylistID = oldPlaylistURL.substring(34, 56);

    console.log(from);
    console.log(to);
    console.log(oldPlaylistID);
    console.log(name);

    var url =
      "http://localhost:8080/createNew?fromPlatform="+from+"&toPlatform="+to+"&oldPlaylistID="+oldPlaylistID+"&newPlaylistName="+name;

    axios
      .get(url)
      .then((res) => {
        setReturnURL("You can find your playlist at: " + res.data['rez']);
      })
      .catch((error) => {
        console.error(error);
      });
  }
  // useEffect(() => {
  //   axios.get('https://jsonplaceholder.typicode.com/posts')
  //     .then(response => {
  //       setReturnURL(response.data);
  //     })
  //     .catch(error => {
  //       console.error(error);
  //     });
  // }, []);

  return (
    <div className="App">
      <header className="App-header">
        <TextField
          font="small"
          id="filled-basic"
          label="Link of the playlist to be converted"
          variant="filled"
          value={oldPlaylistURL}
          onChange={(e) => {
            setOldPlaylistURL(e.target.value);
          }}
        />
        <TextField
          id="filled-basic"
          label="New playlist name? (no spaces)"
          variant="filled"
          value={name}
          onChange={(e) => {
            setName(e.target.value);
          }}
        />
        <TextField
          inputProps={{ maxLength: 1 }}
          id="filled-basic"
          label="Convert from"
          variant="filled"
          value={convertFrom}
          onChange={(e) => {
            setConvertFrom(e.target.value);
          }}
        />
        <TextField
          inputProps={{ maxLength: 1 }}
          id="filled-basic"
          label="Convert to"
          variant="filled"
          value={convertTo}
          onChange={(e) => {
            setConvertTo(e.target.value);
          }}
        />

        <p>type Y for youtube music or S for spotify</p>

        <Button variant="contained" onClick={handleClick}>
          Go?
        </Button>

        <p>{returnURL}</p>
      </header>
    </div>
  );
}

export default App;
