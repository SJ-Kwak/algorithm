function solution(new_id) {
    let answer = '';
    // 1단계
    new_id = new_id.toLowerCase();
    // 2단계
    new_id = new_id.replace(/[^a-z0-9._-]+/g, '')
    // 3단계
    new_id = new_id.replace(/[..]{2,}/g, '.')
    // 4단계
    new_id = new_id.replace(/^\.+|\.+$/g, '')
    // 5단계
    new_id.length === 0 && (new_id = 'a')
    // 6단계
    new_id.length > 15 && (
        new_id = new_id.slice(0, 15).replace(/\.$/g, '')
    )
    // 7단계
    new_id.length < 3 && (
        new_id += new_id.charAt(new_id.length - 1).repeat(3-new_id.length)
    )
    return new_id;
}