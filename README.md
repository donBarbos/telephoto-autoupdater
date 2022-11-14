<h1 align="right"><em>Auto Update Telegram Profile Photo</em></h1>

<p align="right">
<a href="https://github.com/donBarbos/telegram-bot-template/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg?style=plastic" alt="License: AGPL v3"></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=plastic" alt="Code style: black"></a>
<p>

## ℹ️ Description

**_Application allows you to set an profile photo by getting it from a local path or from the generator site_**

<details>
<summary><em>example list of picture generators</em></summary>
  <ul>
    <li> https://thispersondoesnotexist.com/image </li>
    <li> https://loremflickr.com/360/360 </li>
    <li> https://placekitten.com/640/640 </li>
    <li> https://www.fillmurray.com/720/720 </li>
    <li> https://picsum.photos/1024/1024 </li>
  </ul>
</details>

## 🚀 Getting Started

### How to start

0. first you need to get api id and hash from [telegram.org](https://my.telegram.org)

1. create a config file `.env` from a template `.env.example`
    ```bash
    cp .env .env.example
    ```
2. set variables in `.env` file ([see](#%EF%B8%8F-settings) for more information)

3. install dependencies
    ```bash
    python3 -m pip install -r requirements.txt
    ```
4. start the bot
    ```bash
    python3 -m bot
    ```

## ⚙️ Settings

|       variables       | description                                                               |
| :-------------------: | ------------------------------------------------------------------------- |
|       `API_ID`        | Telegram API variable ([to get](https://my.telegram.org))                 |
|      `API_HASH`       | Telegram API variable ([to get](https://my.telegram.org))                 |
|     `PHOTOS_PATH`     | Path to image folder (name of dir)                                        |
|    `TIME_INTERVAL`    | Profile photo update interval (in hours)                                  |
| `REMOVE_FORMER_PHOTO` | Specifies whether to delete the previous photo before updating the avatar |
|      `IMAGE_URL`      | Image generator website URL (see list above)                              |
|        `NAME`         | Any name for your session                                                 |

## 👷🏾 Contributing

First off, thanks for taking the time to contribute! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. `Fork` this repository
2. Create a `branch`
3. `Commit` your changes
4. `Push` your `commits` to the `branch`
5. Submit a `pull request`

## 📝 License

Distributed under the GPL-3.0 license. See [`LICENSE`](./LICENSE) for more information.

## 📢 Contact

[donbarbos](https://github.com/donBarbos): [@donBarbos](https://t.me/donbarbos)
