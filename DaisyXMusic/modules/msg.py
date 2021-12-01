# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Merhaba 👋 [{}](tg://user?id={})!**\n\n🤖 Merhaba ✋ Sesli Sohbetlerde Muzik oynatmanıza Yardımcı Olabilen Bir Müzik Botuyum Beni Grubunuza veya Kanalınıza Ekleyerek Kullanabilirsiniz. \n\n✅ Yardım için /help Komutunu Yollayabilirsiniz."
    HELP_MSG = [
        ".",
        f"""
**Hey 👋 Giriş Ekranına Geri Dön {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",
        f"""
**Setting up**

1) Grup'a yönetici olarak ekle
2) Sesli sohbet başlat
3) /play komutu ile istediğin şarkıyı başlat
*) Olası durumlarda Asistanı Kendi Elinizle Eklemeniz Gerekebilir @{ASSISTANT_NAME} Asistana bu kullanıcı adı ile ulaşabilirsiniz

**For Channel Music Play**
1) Kanalına Yönetici olarak Ekle
2) Bu Komutu /userbotjoinchannel yolla ve Asistanın kanala katılmasını sağla
3) komutlar ile botun keyfini çıkar
""",
        f"""
**Commands**

**=>> Song Playing 🎧**

- /play: Müzik oynatmanızı sağlar
- /play [yt url] : Youtube url si ile müzik oynat
- /play [reply yo audio]: Gruba yada kanala atılan müziği cevaplayarak yolla ve oynat
- /splay: Jio Savn İle sarkı çal
- /ytplay: Youtube İle şarkı çal

**=>> Playback ⏯**

- /player: Oynatıcı Ayarları
- /skip: Mevcut parçayı atlar
- /pause: Mevcut sarkıyı durdurur
- /resume: Mevcut Sarkı Devam eder
- /end: Mevcut sarkıyı kapatır
- /mute: Asistanı Susturur
- /unmute: Asistanın sesini açar
- /current: Gecerli çalmakta olaan parçayı gosterir
- /playlist: Calma Listesini gösterir

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /cmute - mute song play
- /mute - mute song play
- /unmute - mute song play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",
        f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
        f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",
        f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

""",
    ]
