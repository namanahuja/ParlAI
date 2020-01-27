#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

task_config = {}

end_info = """

<h4><span style="color:blue"><b>Guidelines</b></span></h4>
1. Your response should aim to <span style='color:red'><b>continue the conversation</b></span> or to <span style='color:red'><b>answer the client’s question</b></span>.
<br>
2. Please <span style='color:red'><b>avoid very short responses</b></span> such as only saying 'No', 'Yes', and 'Okay' as they are not informative.
<br>
3. Please do not send any message that could make others <span style='color:red'><b>uncomfortable</b></span>,
including any level of discrimination, racism, sexism and offensive
religious/politics comments, otherwise the submission will be rejected.
<br>
<br>
<br>
<h4><span style="color:blue"><b>Reward/Bonus</b></span></h4>
You will receive <span style='color:red'><b>$0.25</b></span> for finishing a task session of <span style='color:red'><b>5 minutes</b></span> 
with <span style='color:red'><b>at least 5 successfully completed conversations</b></span>. Your responses will be evaluated by other human workers. 
Note that we will reject your HIT if you quit before 5 minutes or did not finish 5 conversations with informative responses.
<br>
We expect you to finish <span style='color:red'><b>as many conversations as possible while maintaining the quality of your responses</b></span>. 
The top-performing 10% of the HITs, counting both the number of finished conversations and the quality of their responses, will be awarded a bonus of $0.50.
<br>
<br>
"""

"""A short and descriptive title about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT title appears in search results,
and everywhere the HIT is mentioned.
"""
task_config['hit_title'] = 'Chatting with People Online'


"""A description includes detailed information about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT description appears in the expanded
view of search results, and in the HIT and assignment screens.
"""
task_config['hit_description'] = 'You will chat with another person, either freely '
'or in the context of information provided for each response.'


"""One or more words or phrases that describe the HIT, separated by commas.
On MTurk website, these words are used in searches to find HITs.
"""
task_config['hit_keywords'] = 'chat,dialog'


"""A detailed task description that will be shown on the HIT task preview page
and on the left side of the chat page. Supports HTML formatting.
"""
task_config[
    'task_description'
] = '''
Imagine your work is to chat with many people online. We will provide you with some ongoing conversations between you and another person (referred to as “Client”), and you need to provide appropriate and informative responses to them.
<br>
<br>
<h4><span style='color:blue'><b>Example Conversation</b></span></h4>
<b>Client</b>: Hi! I really like board games.
<br>
<b>You</b>: Oo, what type of board games?
<br>
<b>Client</b>: I like strategy games, especially ones that are sci-fi
<br>
<b>You</b>: <span style='color:red'><b>(... you need to provide your response ...)</b></span>

<br>
<br>
{}
If you are ready, please click "Accept HIT" to start this task.
'''.format(
    end_info
)

task_config[
    'wizard_onboarding'
] = '''
<h2>You have just met the other person, who seems quite curious, and you are
eager to discuss a topic with them!</h2>
<br>

Provide relevant and meaningful responses, and in
general have an engaging conversation.
<br>
<br>

After sending a response, you will be able to click the
DONE button to finish the chat.

<b>Note: we will reward engaging and knowledgeable chats with BONUSES.</b>
<br>
<br>

<h4><span style="color:blue"><b>Sample Conversation</b></span></h4>
<b>Partner</b>: Hi! I really like board games.
<br>
<b>You</b>: Oo, what type of board games?
<br>
<b>Partner</b>: I like strategy games, especially ones that are sci-fi
<br>
<b>You</b>: I love Risk, but it takes place on earth, so not sci-fi, and it
takes forever

<br>
<br>
{}
<br>
<br>
'''.format(
    end_info
)
task_config[
    'apprentice_onboarding'
] = '''
<h2> You have just met the other person, who seems quite knowledgable, and you are
curious to discuss a topic with them!</h2>
<br>
You will try to learn from your conversation partner about a topic that one of you will
choose. Feel free to dive deep on specifics - your partner will have access to
external information that will help them craft their response.
<br>
<br>
After a minimum number of turns, you will be able to click the DONE button
to finish the chat.

<br>
<br>
<h4><span style="color:blue"><b>Conversation Outline</b></span></h4>
Thus, a conversation will proceed as follows: (from your perspective)<br>
<ol>
<li>You or your partner will pick an initial conversation topic from the
list provided, and open the conversation.</li>
<li>You will try to learn about the chosen topic</li>
<li>After you send a message, your partner will respond, continuing the
conversation and hopefully providing more information about the topic.</li>
</ol>
<br>
And the conversation continues until the minimum number of chat turns is
reached, at which point you will evaluate the quality of your conversation
partner, based on how relevant, engaging, and <b>knowledgeable</b> they were.
<br>
<br>
<h4><span style="color:blue"><b>Sample Conversation</b></span></h4>
<br>
<br>
<b>You</b>: Hi! I really like board games.
<br>
<b>Them</b>: Oo, what type of board games?
<br>
<b>You</b>: I like strategy games, especially ones that are sci-fi
<br>
<b>Them</b>: I love Risk, but it takes place on earth, so not sci-fi,
and it takes forever
<br>
<b>You</b>: Right? How do you feel about cards against humanity?
<br>
<b>Them</b>: Cards against humanity is fun but a little too risque for me
<br>
<br>
{}
'''.format(
    end_info
)
