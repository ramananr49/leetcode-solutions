import Playlist from "./playlist.js";
import {expect} from "chai";

describe("Playlist unit test", () => {

    let playlist;

    beforeEach(() => {
        playlist = new Playlist("My Playlist")
    })

    it("Verify that Songs is able to add", () => {
        const song_added = playlist.addSong("Song A")
        expect(song_added).to.equal(true)
        expect(playlist.getSongs()).to.contain("Song A")
    })

    it("Verify that Duplicate Songs cannot allowed", () => {
        playlist.addSong("Song A")
        expect(playlist.addSong("Song A")).to.be.false
    })

    it("Verify that Song is able to remove", () => {
        playlist.addSong("Song A")
        expect(playlist.removeSong("Song A")).to.be.true
        expect(playlist.getSongs()).not.contain("Song A")
    })

    it("Verify that false will return when removing non exisitng song", () => {
        playlist.addSong("Song A")
        playlist.addSong("Song B")
        expect(playlist.removeSong("Song C")).to.be.false;
        expect(playlist.getTotalSongs()).to.equal(2)
    })

    it("Verify that get songs return all the songs from Playlist", () => {
        playlist.addSong("a");
        playlist.addSong("b");
        playlist.addSong("c");
        playlist.addSong("d");
        expect(playlist.getSongs()).to.eql([ 'a', 'b', 'c', 'd' ])

    })

    it("Verify that get Total Song count from Playlist", () => {
        playlist.addSong("Hello");
        playlist.addSong("World");
        playlist.addSong("JavaScript");
        expect(playlist.getTotalSongs()).to.eq(3)

    })
        
})