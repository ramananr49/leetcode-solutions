export default class Playlist {

    constructor(name){
        this.name = name
        this.songs = []
    }

    addSong(song) {
        if (!this.songs.includes(song)){
            this.songs.push(song)
            return true
        }
        return false
    }

    removeSong(song) {
        const index = this.songs.indexOf(song)
        if (index !== -1) {
            this.songs.splice(index, 1)
            return true
        }
        return false
    }

    getSongs() {
        return this.songs
    }

    getTotalSongs() {
        return this.songs.length
    }
}