import logging, random, requests, urllib
from .plugin import Plugin

log = logging.getLogger("discord")

memes = [
"One Does Not Simply",
"Batman Slapping Robin",
"The Most Interesting Man In The World",
"Ancient Aliens",
"Futurama Fry",
"X, X Everywhere",
"Leonardo Dicaprio Cheers",
"Brace Yourselves X is Coming",
"First World Problems",
"But Thats None Of My Business",
"Y U No",
"Creepy Condescending Wonka",
"Bad Luck Brian",
"That Would Be Great",
"Success Kid",
"Third World Skeptical Kid",
"Grumpy Cat",
"Captain Picard Facepalm",
"Doge",
"Matrix Morpheus",
"Boardroom Meeting Suggestion",
"X All The Y",
"Picard Wtf",
"Face You Make Robert Downey Jr",
"Black Girl Wat",
"The Rock Driving",
"Am I The Only One Around Here",
"Evil Toddler",
"Dr Evil Laser",
"Philosoraptor",
"Maury Lie Detector",
"Too Damn High",
"Disaster Girl",
"Third World Success Kid",
"Finding Neverland",
"Confession Bear",
"Aint Nobody Got Time For That",
"Ill Just Wait Here",
"Grandma Finds The Internet",
"Say That Again I Dare You",
"Awkward Moment Sealion",
"Skeptical Baby",
"Dont You Squidward",
"Laughing Men In Suits",
"10 Guy",
"Yo Dawg Heard You",
"And everybody loses their minds",
"Bad Pun Dog",
"Sparta Leonidas",
"Conspiracy Keanu",
"Put It Somewhere Else Patrick",
"Back In My Day",
"Aaaaand Its Gone",
"Confused Gandalf",
"Kill Yourself Guy",
"Overly Attached Girlfriend",
"Scumbag Steve",
"Mugatu So Hot Right Now",
"You The Real MVP",
"I Should Buy A Boat Cat",
"Yall Got Any More Of",
"Liam Neeson Taken",
"Ryan Gosling",
"Spiderman Computer Desk",
"Rick and Carl",
"Socially Awesome Awkward Penguin",
"See Nobody Cares",
"Buddy Christ",
"Imagination Spongebob",
"Pepperidge Farm Remembers",
"Leonardo Dicaprio Wolf Of Wall Street",
"Archer",
"Ermahgerd Berks",
"Jackie Chan WTF",
"Simba Shadowy Place",
"Peter Griffin News",
"Kevin Hart The Hell",
"Sudden Clarity Clarence",
"Angry Baby",
"So I Got That Goin For Me Which Is Nice",
"Obi Wan Kenobi",
"Gollum",
"Shut Up And Take My Money Fry",
"Satisfied Seal",
"Star Wars No",
"Buddy The Elf",
"Surprised Koala",
"Unpopular Opinion Puffin",
"Brian Williams Was There",
"I Too Like To Live Dangerously",
"Spiderman Peter Parker",
"Keep Calm And Carry On Red",
"Pissed Off Obama",
"Rick and Carl Long",
"Ron Burgundy",
"Look At All These",
"What Do We Want",
"Peter Parker Cry",
"Jack Sparrow Being Chased",
"Dwight Schrute",
]

class Memes(Plugin):
	"""
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

	title = "Such memes, much plugin"
	desc = "What is my purpose?"

	def __init__(self): pass

	def on_ready(self, client): pass
	def on_message(self, client, message):
		if message.content.startswith("!meme"):
			rand = random.randint(0, len(memes))

			log.info("random: " + str(rand))
			me = memes[rand]
			apimeme = "http://apimeme.com/meme?meme=%s&top=%s&bottom=%s"
			top = message.content.split("\"")[1]
			bot = message.content.split("\"")[3]
			meme = apimeme % (
				urllib.quote(me),
				urllib.quote(top), #message.content.split(";")[0][len("!meme "):]),
				urllib.quote(bot)) #message.content.split(";")[1]))

			client.send_message(message.channel, meme)

	def on_socket_closed(self,client): pass

	def on_message_delete(self, client, message): pass
	def on_message_edit(self, client, before, after): pass
	def on_status(self, client, member): pass
	
	def on_channel_delete(self, client, channel): pass
	def on_channel_create(self, client, channel): pass
	def on_channel_update(self, client, channel): pass
	
	def on_member_join(self, client, member): pass
	def on_member_remove(self, client, member): pass
	def on_member_update(self, client, member): pass
	
	def on_server_create(self, client, server): pass
	def on_server_delete(self, client, server): pass
	
	def on_server_role_create(self, client, server, role): pass
	def on_server_role_delete(self, client, server, role): pass
	def on_server_role_update(self, client, role): pass

	def on_voice_state_update(self, client, member): pass