import "./App.css";
import {
  TextField,
  Button,
  Box,
  MenuItem,
  Select,
  InputLabel,
  FormControl,
} from "@mui/material";
import { useState } from "react";
import axios from "axios";

function App() {
  const [name, setName] = useState("dattebayo");
  const [oldPlaylistURL, setOldPlaylistURL] = useState("");
  const [convertFrom, setConvertFrom] = useState("");
  const [convertTo, setConvertTo] = useState("");
  const [returnURL, setReturnURL] = useState("");
  const [bug, setBug] = useState(false);
  const [isNotValidURL, setIsNotValidURL] = useState(false);
  const [doesURLNotMatch, setDoesURLNotMatch] = useState(false);
  const [notFilled, setNotFilled] = useState(false);

  function handleClick() {
    let oldPlaylistID = "";

    if (convertFrom === "" || convertTo === "" || oldPlaylistURL === "") {
      setNotFilled(true);
      return;
    }
    setNotFilled(false);

    if (convertFrom === convertTo) {
      setBug(true);
      return;
    }
    setBug(false);

    const youtubeMusicPlaylistIdRegex =
      /\b(https?:\/\/[^/]*\byoutube\.com\/playlist\?list=(.*?)(?:&|$)\b)/i;
    const ytmMatch = youtubeMusicPlaylistIdRegex.exec(oldPlaylistURL);
    let ytmLink = true;

    if (ytmMatch) {
      oldPlaylistID = ytmMatch[2];

      console.log("The playlist ID is:", oldPlaylistID);
    } else {
      ytmLink = false;
      console.log("The string is not a YouTube Music playlist URL.");
    }

    const spotifyPlaylistIdRegex =
      /\b(https?:\/\/[^\/]*\bspotify\.com\/playlist\/([^\s?]+)\b)/i;
    const spotifyMatch = spotifyPlaylistIdRegex.exec(oldPlaylistURL);
    let spotifyLink = true;

    if (spotifyMatch) {
      oldPlaylistID = spotifyMatch[2];

      console.log("The playlist ID is:", oldPlaylistID);
    } else {
      spotifyLink = false;
      console.log("The string is not a Spotify playlist URL.");
    }

    if (!spotifyLink && !ytmLink) {
      setIsNotValidURL(true);
      return;
    }

    setIsNotValidURL(false);

    if (
      (convertFrom === "Spotify" && !spotifyLink) ||
      (convertFrom === "YouTubeMusic" && !ytmLink)
    ) {
      setDoesURLNotMatch(true);
      return;
    }
    setDoesURLNotMatch(false);

    console.log(convertFrom);
    console.log(convertTo);
    console.log(oldPlaylistID);
    console.log(name);

    var url =
      "http://localhost:8080/createNew?fromPlatform=" +
      convertFrom +
      "&toPlatform=" +
      convertTo +
      "&oldPlaylistID=" +
      oldPlaylistID +
      "&newPlaylistName=" +
      name;

    axios
      .get(url)
      .then((res) => {
        setReturnURL(res.data["rez"]);
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

  const handleFromChange = (event: SelectChangeEvent) => {
    setConvertFrom(event.target.value);
  };
  const handleToChange = (event: SelectChangeEvent) => {
    setConvertTo(event.target.value);
  };

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
        <div className="Hor-Row">
          <Box sx={{ minWidth: 160 }}>
            <FormControl fullWidth>
              <InputLabel id="demo-simple-select-label">
                Convert From
              </InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={convertFrom}
                label="Convert From"
                onChange={handleFromChange}
              >
                <MenuItem value="YouTubeMusic">YouTubeMusic</MenuItem>
                <MenuItem value="Spotify">Spotify</MenuItem>
              </Select>
            </FormControl>
          </Box>
          <Box sx={{ minWidth: 160 }}>
            <FormControl fullWidth>
              <InputLabel id="demo-simple-select-label">Convert To</InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={convertTo}
                label="Convert To"
                onChange={handleToChange}
              >
                <MenuItem value="Spotify">Spotify</MenuItem>
                <MenuItem value="YouTubeMusic">YouTubeMusic</MenuItem>
              </Select>
            </FormControl>
          </Box>
        </div>

        <Button variant="contained" onClick={handleClick}>
          Go?
        </Button>

        {bug && (
          <p style={{ color: "red", fontSize: "16px" }}>
            To and From cannot be same
          </p>
        )}
        {isNotValidURL && (
          <p style={{ color: "red", fontSize: "16px" }}>
            Invalid playlist link
          </p>
        )}
        {doesURLNotMatch && (
          <p style={{ color: "red", fontSize: "16px" }}>
            The given URL does not match the source chosen
          </p>
        )}
        {notFilled && (
          <p style={{ color: "red", fontSize: "16px" }}>
            The fields cannot be empty
          </p>
        )}

{returnURL && (
          <p style={{ color: "black", fontSize: "16px" }}>
            You can find your playlist at:
          </p>
        )}

        <a href={returnURL} style={{ color: "blue", fontSize: "16px" }}>{returnURL}</a>
      </header>
    </div>
  );
}

export default App;
