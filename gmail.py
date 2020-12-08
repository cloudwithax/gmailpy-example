import gmailpy
import asyncio

client = gmailpy.Client("<your email here>", "<your email password here>")


async def send_email():
    await asyncio.sleep(3)
    print('-------------------------------------------')
    print('   _____                 _ _               ')
    print('  / ____|               (_) |              ')
    print(' | |  __ _ __ ___   __ _ _| |  _ __  _   _ ')
    print(" | | |_ | '_ ` _ \ / _` | | | | '_ \| | | |")
    print(' | |__| | | | | | | (_| | | |_| |_) | |_| |')
    print('  \_____|_| |_| |_|\__,_|_|_(_) .__/ \__, |')
    print('                              | |     __/ |')
    print('                              |_|    |___/ ')
    print('')
    print('         Made by cloudwithax 2020          ')
    print('-------------------------------------------')
    await asyncio.sleep(2)
    email = input("What email would you like to send this to?\n")
    print(f'Reciever set to {email}')
    await asyncio.sleep(1)
    body = input("What would you like the body of the email to be?\n")
    print(f'Body set to {body}')
    await asyncio.sleep(1)
    subject = input("What would you like the subject to be? (Type 'none' for no subject)\n")
    if subject == 'none':
        print('Subject set to none')
    else:
        print(f'Subject set to {subject}')
    await asyncio.sleep(1)
    bcc = input("Who should be included in the BCC line? (Seperate each e-mail with a space, type 'none' for no BCC)\n")
    await asyncio.sleep(1)
    if not bcc == 'none':
        bclist = bcc.split()
        print(f"BCC line set to {','.join(bclist)}")
    else:
        print('BCC line set to none')
    await asyncio.sleep(1)
    print(f'Now sending e-mail to {email}...')
    if subject == 'none' and bcc == 'none':
        await client.send(f'{email}', f'{body}')
    elif bcc == 'none':
        await client.send(f'{email}', f'{body}', f'{subject}')
    else:
        await client.send(f'{email}', f'{body}', f'{subject}', f'{bclist}')
    print('The e-mail has been successfully sent!')
    await asyncio.sleep(2)
    return


asyncio.run(send_email())
